import React from "react";
import { Link } from "react-router";
import Historgram from "../components/Historgram";

const Tracker = () => {
  return (
    <div>
      <div className="flex items-center justify-center h-screen bg-green-300">
        <div className="bg-white rounded-lg shadow-lg w-full max-w-md p-8">
          <Historgram />
          <div className="mt-4 flex justify-between">
            <Link to="/" className="text-gray-600 font-bold text-green-600">
              HOME
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

export default Tracker;
