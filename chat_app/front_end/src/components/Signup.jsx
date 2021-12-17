import React from "react";
import { useState, useRef } from "react";
import Username from "./Username.jsx";
import useInputValidator from "../hooks/useInputValidator.jsx";

function SignUp() {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [valid, setValid] = useState({
    first_name: false,
    last_name: false,
    username: false,
    password: false,
    confirmed_password: false,
  });

  return (
    <div className="flex flex-col items-center lg:w-1/2 mx-auto ">
      <h1 className="text-3xl mt-12 mb-3 font-semibold ">Create Account</h1>
      <form className="flex flex-col pt-10 border-blue-700 border-t-2 w-full px-5 ">
        <label htmlFor="first_name" className="mb-2">
          First name
        </label>
        <div className="flex flex-col mb-4">
          <input
            id="first_name"
            className="h-15 rounded-md pl-3 p-3 bg-gray-200"
            placeholder="first name"
            autoFocus
            value={first_name}
            onChange={(e) => {
              if (useInputValidator(e.target, first_name, valid)) {
                setFirstName(e.target.value);
                setValid({
                  first_name: true,
                });
              } else {
                setValid({
                  first_name: false,
                });
              }
            }}
          />
          <span className="ml-1 font-mono mt-1 font-light text-xs"></span>
        </div>

        <label htmlFor="last_name" className="mb-2">
          Last name
        </label>
        <div className="flex flex-col mb-4">
          <input
            id="last_name"
            className="h-12 rounded-md pl-3 p-3 bg-gray-200"
            placeholder="last name"
            value={last_name}
            onChange={(e) => {
              if (useInputValidator(e.target, last_name, valid)) {
                setLastName(e.target.value);
                setValid({
                  last_name: true,
                });
              } else {
                setValid({
                  last_name: false,
                });
              }
            }}
          />
          <span className="ml-1 font-mono mt-1 font-light text-xs"></span>
        </div>

        <Username
          username={username}
          valid={valid}
          setValid={setValid}
          setUsername={setUsername}
        />

        <label htmlFor="password" className="mb-2 mt-4">
          Password
        </label>
        <div className="flex flex-col mb-4">
          <input
            id="password"
            value={password}
            className="h-12 rounded-md p-3 pl-3 bg-gray-200"
            placeholder="password"
            type="password"
            onChange={(e) => {
              if (useInputValidator(e.target, password, valid)) {
                setPassword(e.target.value);
                setValid({
                  password: true,
                });
              } else {
                setValid({
                  password: false,
                });
              }
            }}
          />
          <span className="ml-1 font-mono mt-1 font-light text-xs"></span>
        </div>

        <label htmlFor="confirmed_password" className="mb-2">
          Confirm password
        </label>
        <div className="relative flex flex-col">
          <input
            id="confirmed_password"
            className="h-12 rounded-md p-3 pl-3 bg-gray-200"
            placeholder="Re-enter password"
            type="password"
            onChange={(e) => {
              const confirmed_password = e.target.value;

              if (password !== "") {
                const element = document.getElementById("confirmed_password");

                if (password !== confirmed_password) {
                  element.classList.add("ring-2");
                  setValid({
                    confirmed_password: false,
                  });
                } else {
                  element.classList.remove("ring-2");
                  setValid({
                    confirmed_password: true,
                  });
                }
              }
              if (useInputValidator(e.target, confirmed_password, valid)) {
                setValid({
                  confirmed_password: true,
                });
              } else {
                setValid({
                  confirmed_password: false,
                });
              }
            }}
          />
          <span className="ml-1 font-mono mt-1 font-light text-xs"></span>
        </div>
      </form>
      <button
        // onClick={}
        className="w-3/5 text-white rounded-full h-16 mt-8 mb-9 bg-gray-400 font-medium text-lg"
      >
        Sign up
      </button>
    </div>
  );
}

export default SignUp;
