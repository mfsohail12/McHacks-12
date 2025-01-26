import React, { useEffect, useState } from "react";
import logo from "../assets/logo.webp";
import { HiQuestionMarkCircle } from "react-icons/hi";

const HomePage = () => {
  const [data, setData] = useState(null);
  const userId = "anon_1234";
  const [position, setPosition] = useState(1);
  const [phase, setPhase] = useState("");
  const [triage, setTriage] = useState("");

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
    const interval = setInterval(fetchData, 60000);
    return () => clearInterval(interval);
  }, []);

  if (data) {
    setPosition(data.queue_position.global);
    setPhase(data.status.current_phase);
    setTriage(data.triage_category);
  }

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
            <h3 className="text-3xl font-bold text-gray-800">CURRENT PHASE</h3>
            <p className="text-2xl uppercase text-gray-500 mt-1 mb-7 font-bold">
              {data ? data.status.current_phase : "loading ..."}
            </p>
            <div className="flex items-center">
              <h3 className="text-3xl font-bold text-gray-800">TRIAGE LEVEL</h3>
              <HiQuestionMarkCircle className="text-2xl ml-2" />
            </div>
            <p className="text-2xl uppercase text-gray-500 mt-1 mb-3 font-bold">
              {data ? data.triage_category : "loading ..."}
            </p>
          </div>
          <div className="mt-4 flex justify-between">
            <span className="text-gray-600">TRACKER</span>
            <span className="text-gray-600">GAME LOBBY</span>
          </div>
        </div>
      </div>
    </div>
  );
};

// const HomePage = () => {
//   return (
//     <div className="main-container w-[1440px] h-[1024px] bg-[#fff] relative overflow-hidden mx-auto my-0">
//       <div className="w-[1440px] h-[135px] bg-[rgba(109,164,65,0.81)] absolute top-0 left-0 z-[4]">
//         <span className="flex h-[65px] justify-start items-start font-['Bebas_Neue'] text-[64px] font-normal leading-[65px] text-[#e3f4aa] absolute top-[38px] left-[1163px] text-left whitespace-nowrap z-[4]">
//           Game Lobby
//         </span>
//         <span className="flex h-[58px] justify-start items-start font-['Bebas_Neue'] text-[64px] font-normal leading-[58px] text-[#e3f4aa] absolute top-[38px] left-[921px] text-left whitespace-nowrap z-[3]">
//           Tracker
//         </span>
//       </div>
//       <div className="w-[1440px] h-[1017px] bg-[url(../assets/images/62cf214b-8e41-4460-91b8-d87ff2ab1ba8.png)] bg-cover bg-no-repeat absolute top-[7px] left-0" />
//       <div className="w-[1833px] h-[1570px] absolute top-[7px] left-[33px] z-[13]">
//         <div className="w-[276px] h-[284px] bg-[url(../assets/images/8c162c5b-f792-4f52-bdc1-c7006c06b953.png)] bg-cover bg-no-repeat absolute top-0 left-0 z-[5]" />
//         <div className="w-[223px] h-[224px] bg-[url(../assets/images/dd18a878d2cb2251a8efb8ceb52be3041d5ce4bc.png)] bg-cover bg-no-repeat absolute top-[30px] left-[26px] z-[6]" />
//         <span className="flex h-[79px] justify-start items-start font-['Bebas_Neue'] text-[55px] font-normal leading-[66px] text-[#1f2a15] tracking-[1.65px] absolute top-[175px] left-[317px] text-left whitespace-nowrap z-[7]">
//           Your Position in Line is:
//         </span>
//         <div className="w-[1310px] h-[1310px] bg-[url(../assets/images/47b713ab-8b3a-432c-a4ad-821f39efc6ff.png)] bg-cover bg-no-repeat rounded-[50%] absolute top-[260px] left-[523px] z-[8]" />
//         <div className="w-[1200px] h-[1150px] bg-[url(../assets/images/4c23ffed-34bf-4dbc-b8d5-4c5af280faa2.png)] bg-cover bg-no-repeat absolute top-[301px] left-[594px] z-[9]" />
//         <div className="w-[1100px] h-[1012.917px] bg-[url(../assets/images/551152e2-d4e3-4704-9c77-24090e4fa5e7.png)] bg-cover bg-no-repeat absolute top-[344px] left-[677px] z-10" />
//         <span className="flex w-[436px] h-[341px] justify-start items-start font-['Bebas_Neue'] text-[70px] font-normal leading-[84px] text-[#1f2a15] tracking-[2.1px] absolute top-[535px] left-[901px] text-left z-[11]">
//           Your Current Phase:
//         </span>
//         <span className="flex w-[355px] h-[342px] justify-start items-start font-['Bebas_Neue'] text-[70px] font-normal leading-[84px] text-[#1f2a15] tracking-[2.1px] absolute top-[744px] left-[897px] text-left z-[12]">
//           Your Triage Level:
//         </span>
//         <span className="flex w-[314px] h-[54px] justify-start items-start font-['Be_Vietnam'] text-[24px] font-normal leading-[35.064px] text-[#000] tracking-[0.72px] absolute top-[963px] left-[1115px] text-left underline z-[13]">
//           What does this mean?
//         </span>
//       </div>
//       <div className="w-[1440px] h-[10px] bg-[url(../assets/images/e3a70159-d8be-4e0f-b3e9-3a6d1c685d15.png)] bg-cover bg-no-repeat absolute top-[130px] left-0 z-[2]" />
//     </div>
//   );
// };

export default HomePage;
