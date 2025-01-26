import React from "react";

const GameHub = () => {
  return (
    <div className="min-h-screen bg-gray-100 flex items-center justify-center">
      <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4 p-4 w-full">
        {Array.from({ length: 9 }).map((_, index) => (
          <div
            key={index}
            className="bg-gray-300 h-48 flex items-center justify-center w-full"
          >
            <span className="text-gray-500">Game {index + 1}</span>
          </div>
        ))}
      </div>
    </div>
  );
};

export default GameHub;
