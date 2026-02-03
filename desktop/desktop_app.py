import sys
import requests
from PyQt5.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QPushButton,
    QFileDialog, QLabel, QHBoxLayout, QFrame
)
from PyQt5.QtCore import Qt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class Dashboard(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chemical Equipment Dashboard (Desktop)")
        self.setGeometry(200, 200, 1000, 600)

        self.layout = QVBoxLayout()

        # Upload Button
        self.upload_btn = QPushButton("Upload CSV")
        self.upload_btn.clicked.connect(self.upload_file)
        self.layout.addWidget(self.upload_btn)

        # Summary Section
        self.summary_layout = QHBoxLayout()
        self.total_label = self.create_card("Total: -")
        self.flow_label = self.create_card("Avg Flowrate: -")
        self.pressure_label = self.create_card("Avg Pressure: -")
        self.temp_label = self.create_card("Avg Temp: -")

        self.summary_layout.addWidget(self.total_label)
        self.summary_layout.addWidget(self.flow_label)
        self.summary_layout.addWidget(self.pressure_label)
        self.summary_layout.addWidget(self.temp_label)

        self.layout.addLayout(self.summary_layout)

        # Chart Area
        self.figure = Figure()
        self.canvas = FigureCanvas(self.figure)
        self.layout.addWidget(self.canvas)

        self.setLayout(self.layout)

    def create_card(self, text):
        label = QLabel(text)
        label.setAlignment(Qt.AlignCenter)
        label.setFrameShape(QFrame.Box)
        label.setStyleSheet("padding:15px; font-size:14px;")
        return label

    def upload_file(self):
        file_path, _ = QFileDialog.getOpenFileName(self, "Select CSV File")

        if file_path:
            try:
                files = {'file': open(file_path, 'rb')}
                response = requests.post(
                    "http://127.0.0.1:8000/api/upload/",
                    files=files
                )

                data = response.json()

                # Update summary
                self.total_label.setText(f"Total: {data['total']}")
                self.flow_label.setText(f"Avg Flowrate: {data['avg_flowrate']:.2f}")
                self.pressure_label.setText(f"Avg Pressure: {data['avg_pressure']:.2f}")
                self.temp_label.setText(f"Avg Temp: {data['avg_temperature']:.2f}")

                # Update chart
                self.plot_chart(data["type_distribution"])

            except Exception as e:
                print("Error:", e)

    def plot_chart(self, distribution):
        self.figure.clear()

        ax = self.figure.add_subplot(111)
        ax.pie(
            distribution.values(),
            labels=distribution.keys(),
            autopct="%1.1f%%"
        )
        ax.set_title("Equipment Type Distribution")

        self.canvas.draw()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Dashboard()
    window.show()
    sys.exit(app.exec_())