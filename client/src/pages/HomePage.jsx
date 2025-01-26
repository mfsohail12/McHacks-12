import React, { useEffect, useState } from "react";
import logo from "../assets/logo.webp";
import { HiQuestionMarkCircle } from "react-icons/hi";
import { Link } from "react-router-dom";

const HomePage = () => {
  const [data, setData] = useState(null);
  const userId = "anon_1234";

  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch(
          "http://127.0.0.1:5000/api/v1/patient/" + { userId }
        );
        if (!response) throw new Error("null response");
        const result = await response.json();
        setData(result);
      } catch (err) {
        throw new Error("failed retrieving data");
      }
    };

    fetchData();
    const interval = setInterval(fetchData, 2000);
    return () => clearInterval(interval);
  }, []);

  console.log(data);

  return (
    <div>
      <div className="flex items-center justify-center h-screen bg-green-300">
        <div className="bg-white rounded-lg shadow-lg w-full max-w-md p-8">
          <div className="flex items-center">
            <div className="flex-shrink-0">
              <img src={logo} alt="TriageMate Logo" className="w-25" />
            </div>
            <div className="ml-4 h-20">
              <h2 className="text-1xl font-bold text-gray-80">
                YOUR POSITION IN LINE IS
              </h2>
              <h2 className="text-5xl font-bold text-green-300">
                {data ? data.queue_position.global : "loading ..."}
              </h2>
            </div>
          </div>
          <div className="mt-6">
            <div className="flex items-center">
              <h3 className="text-3xl font-bold text-gray-800">
                CURRENT PHASE
              </h3>
              <Link to="http://localhost:8000/phases">
                <HiQuestionMarkCircle className="text-2xl ml-2" />
              </Link>
            </div>
            <p className="text-2xl uppercase text-green-300 mt-1 mb-7 font-bold">
              {data ? data.status.current_phase : "loading ..."}
            </p>
            <div className="flex items-center">
              <h3 className="text-3xl font-bold text-gray-800">TRIAGE LEVEL</h3>
              <Link to="http://localhost:8000/triage">
                <HiQuestionMarkCircle className="text-2xl ml-2" />
              </Link>
            </div>
            <p className="text-2xl uppercase text-green-300 mt-1 mb-10 font-bold">
              {data ? data.triage_category : "loading ..."}
            </p>
          </div>
          <div className="mt-4 flex justify-between">
            <span className="text-gray-600 font-bold text-green-600">
              TRACKER
            </span>
            <span className="text-gray-600 font-bold text-green-600">
              GAME LOBBY
            </span>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
