import React from "react";
import { useState } from "react";
import { AgCharts } from "ag-charts-react";

const Historgram = () => {
  const [chartOptions, setChartOptions] = useState({
    // Data: Data to be displayed in the chart
    data: [
      { triage: "Triage 1", people: 0 },
      { triage: "Triage 2", people: 0 },
      { triage: "Triage 3", people: Math.floor(Math.random() * 10) + 1 },
      { triage: "Triage 4", people: Math.floor(Math.random() * 10) + 1 },
      { triage: "Triage 5", people: Math.floor(Math.random() * 10) + 1 },
    ],
    // Series: Defines which chart type and data to use
    series: [{ type: "bar", xKey: "triage", yKey: "people" }],
    theme: "CentOS",
  });

  return <AgCharts options={chartOptions} />;
};

export default Historgram;
