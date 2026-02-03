import React, { useState } from "react";
import axios from "axios";
import {
  Chart as ChartJS,
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement
} from "chart.js";
import { Pie, Bar } from "react-chartjs-2";

ChartJS.register(
  ArcElement,
  Tooltip,
  Legend,
  CategoryScale,
  LinearScale,
  BarElement
);

function App() {
  const [summary, setSummary] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleUpload = async (e) => {
    const formData = new FormData();
    formData.append("file", e.target.files[0]);

    setLoading(true);

    try {
      const res = await axios.post(
        "http://127.0.0.1:8000/api/upload/",
        formData
      );
      setSummary(res.data);
    } catch (err) {
      alert("Upload failed. Check backend.");
    }

    setLoading(false);
  };

  return (
    <div className="container mt-5">
      <h2 className="text-center mb-4">
        Chemical Equipment Parameter Dashboard
      </h2>

      <div className="card p-4 shadow-sm mb-4">
        <input
          type="file"
          className="form-control"
          onChange={handleUpload}
        />
      </div>

      {loading && <p className="text-center">Processing...</p>}

      {summary && (
        <>
          {/* Summary Cards */}
          <div className="row text-center mb-4">
            <div className="col-md-3">
              <div className="card shadow-sm p-3">
                <h6>Total Equipment</h6>
                <h4>{summary.total}</h4>
              </div>
            </div>

            <div className="col-md-3">
              <div className="card shadow-sm p-3">
                <h6>Avg Flowrate</h6>
                <h4>{summary.avg_flowrate.toFixed(2)}</h4>
              </div>
            </div>

            <div className="col-md-3">
              <div className="card shadow-sm p-3">
                <h6>Avg Pressure</h6>
                <h4>{summary.avg_pressure.toFixed(2)}</h4>
              </div>
            </div>

            <div className="col-md-3">
              <div className="card shadow-sm p-3">
                <h6>Avg Temperature</h6>
                <h4>{summary.avg_temperature.toFixed(2)}</h4>
              </div>
            </div>
          </div>

          {/* Charts */}
          <div className="row">
            <div className="col-md-6">
              <div className="card p-3 shadow-sm">
                <h5 className="text-center">
                  Equipment Type Distribution
                </h5>
                <Pie
                  data={{
                    labels: Object.keys(summary.type_distribution),
                    datasets: [
                      {
                        data: Object.values(
                          summary.type_distribution
                        ),
                        backgroundColor: [
                          "#4e73df",
                          "#1cc88a",
                          "#36b9cc",
                          "#f6c23e",
                          "#e74a3b"
                        ]
                      }
                    ]
                  }}
                />
              </div>
            </div>

            <div className="col-md-6">
              <div className="card p-3 shadow-sm">
                <h5 className="text-center">
                  Type Count (Bar Chart)
                </h5>
                <Bar
                  data={{
                    labels: Object.keys(summary.type_distribution),
                    datasets: [
                      {
                        label: "Count",
                        data: Object.values(
                          summary.type_distribution
                        ),
                        backgroundColor: "#4e73df"
                      }
                    ]
                  }}
                />
              </div>
            </div>
          </div>
        </>
      )}
    </div>
  );
}

export default App;