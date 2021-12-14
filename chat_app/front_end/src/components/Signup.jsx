import React from "react";
import { useState } from "react";
import Username from "./Username.jsx";

function SignUp() {
  const [first_name, setFirstName] = useState("");
  const [last_name, setLastName] = useState("");
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [names, setNames] = useState({list:[]});
  const [UnhappyStyles, setUnhappyStyles] = useState({ display: "none" });
  const [HappyStyles, setHappyStyles] = useState({ display: "none" });


  const string_validator = (input, field_value, call_back) => {

    const last_input_char = input.charAt(input.length - 1);

    if (last_input_char === " ") {
      if (field_value !== "") {
        const last_init_char = field_value.charAt(field_value.length - 1);
        if (last_init_char !== " ") {
          call_back(input);
        }
      }
    } else {
      call_back(input);
    }
  }

  return (
    <div className="flex flex-col items-center lg:w-1/2 mx-auto ">
      <h1 className="text-3xl mt-12 mb-3 font-semibold ">Create Account</h1>
      <form className="flex flex-col pt-10 border-blue-700 border-t-2 w-full px-5 ">
        <label htmlFor="first_name" className="mb-2">
          First name
        </label>
        <input
          id="first_name"
          className="mb-4 h-15 rounded-md pl-3 p-3 bg-gray-200"
          placeholder="first name"
          autoFocus
          value={first_name}
          onChange={(e) => {
            string_validator(e.target.value, first_name, setFirstName);
          }}
        />

        <label htmlFor="last_name" className="mb-2">
          Last name
        </label>
        <input
          id="last_name"
          className="mb-4 h-12 rounded-md pl-3 p-3 bg-gray-200"
          placeholder="last name"
          value={last_name}
          onChange={(e) => {
            string_validator(e.target.value, last_name, setLastName);
          }}
        />

        <Username
          username={username}
          names={names}
          setNames={setNames}
          setUsername={setUsername}
          string_validator={string_validator}
          UnhappyStyles={UnhappyStyles}
          setUnhappyStyles={setUnhappyStyles}
          HappyStyles={HappyStyles}
          setHappyStyles={setHappyStyles}
        />

        <label htmlFor="password" className="mb-2 mt-4">
          Password
        </label>
        <input
          id="password"
          className="mb-4 h-12 rounded-md p-3 pl-3 bg-gray-200"
          placeholder="password"
          type="password"
          onChange={(e) => {
            string_validator(e.target.value, password, setPassword);
          }}
        />

        <label htmlFor="password_confirm" className="mb-2">
          Confirm password
        </label>
        <div className="relative">
          <input
            id="password_confirm"
            className="h-12 rounded-md w-full p-3 ring-red-450 pl-3 bg-gray-200"
            placeholder="Re-enter password"
            type="password"
            onChange={(e) => {
              const confirmed_password = e.target.value;

              if (password !== "") {
                const element = document.getElementById("password_confirm");

                if (password !== confirmed_password) {
                  element.classList.add("ring-2");
                } else {
                  element.classList.remove("ring-2");
                }
              }
            }}
          />
        </div>
      </form>
      <button
        // onClick={}
        className="w-3/5 text-white rounded-full h-16 mt-8 mb-9 bg-blue-700 font-medium text-lg"
      >
        Sign up
      </button>
    </div>
  );
}

export default SignUp;
