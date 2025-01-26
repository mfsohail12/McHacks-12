import React from "react";
import { NavLink } from "react-router-dom";
import logo from "../assets/logo.webp";

const Navbar = () => {
  return (
    <>
      <nav className="bg-green-600">
        <div className="mx-auto max-w-7xl px-2 sm:px-6 lg:px-8">
          <div className="flex h-20 items-center justify-between">
            <div className="flex flex-1 items-center justify-center md:items-stretch md:justify-start">
              {/* <!-- Logo --> */}
              <NavLink className="flex flex-shrink-0 items-center mr-4" to="/">
                <img src={logo} alt="QueueCare Logo" className="h-15 w-auto" />
              </NavLink>
              <div className="md:ml-auto my-auto">
                <div className="flex space-x-10">
                  <NavLink to="/">Tracker</NavLink>
                  <NavLink to="/gamehub">Game Hub</NavLink>
                </div>
              </div>
            </div>
          </div>
        </div>
      </nav>
    </>
  );
};

export default Navbar;
