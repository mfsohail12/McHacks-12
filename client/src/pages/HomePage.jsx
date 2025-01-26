import React, { useEffect, useState } from "react";
import logo from "../assets/logo.webp";
import { HiQuestionMarkCircle } from "react-icons/hi";
import { Link } from "react-router-dom";

const HomePage = () => {
  const [data, setData] = useState(null);
  const [randomUser, setRandomUser] = useState(null);
  const userId = "anon_3396";

  useEffect(() => {
    // const fetchUser = async () => {
    //   try {
    //     const response = await fetch(
    //       "https://ifem-award-mchacks-2025.onrender.com/api/v1/queue"
    //     );
    //     if (!response) throw new Error("null response");
    //     if (response.error) throw new Error(response.error);
    //     const result = await response.json();
    //     setRandomUser(result);
    //   } catch (err) {
    //     throw new Error("failed retrieving data");
    //   }
    // };

    const fetchData = async () => {
      try {
        const response = await fetch(
          "https://ifem-award-mchacks-2025.onrender.com/api/v1/patient/" +
            { userId }
        );
        if (!response) throw new Error("null response");
        if (response.error) throw new Error(response.error);
        const result = await response.json();
        setData(result);
      } catch (err) {
        throw new Error("failed retrieving data");
      }
    };

    fetchData();
    // fetchUser();
    const interval = setInterval(fetchData, 2000);
    return () => clearInterval(interval);
  }, []);

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
              <h2 className="text-5xl font-bold text-green-300">28</h2>
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
              REGISTERED
            </p>
            <div className="flex items-center">
              <h3 className="text-3xl font-bold text-gray-800">TRIAGE LEVEL</h3>
              <Link to="http://localhost:8000/triage">
                <HiQuestionMarkCircle className="text-2xl ml-2" />
              </Link>
            </div>
            <p className="text-2xl uppercase text-green-300 mt-1 mb-10 font-bold">
              3
            </p>
          </div>
          <div className="mt-4 flex justify-between">
            <Link
              to="/tracker"
              className="text-gray-600 font-bold text-green-600"
            >
              TRACKER
            </Link>
            <Link
              to="/gamelobby"
              className="text-gray-600 font-bold text-green-600"
            >
              GAME LOBBY
            </Link>
          </div>
        </div>
      </div>
    </div>
  );
};

export default HomePage;
