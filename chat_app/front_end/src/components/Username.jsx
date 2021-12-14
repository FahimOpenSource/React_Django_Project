import React from "react";
import { useState, useRef, useEffect } from "react";
import axios from "axios";

const Username = ({
  username,
  names,
  setNames,
  setUsername,
  string_validator,
  // UnhappyStyles,
  // setUnhappyStyles,
  // HappyStyles,
  // setHappyStyles
}) => {

  const inputRef = useRef()
  const spanRef = useRef()

  const [infoText, setInfoText] = useState(
    "username may contain letters, digits and @ . + - _"
  );

  useEffect(() => {
    const base_url = "accounts/api/sign-up/";

    axios.get(base_url).then((res) => {
      setNames({list: res.data});
    });
  }, []);

  const handleUniqueValidation = () => {
    console.log("names =>", names.list);
    console.log(username);
    if (username !== "") {
      for (var name of names.list) {
        if (name.includes(username)) {
          console.log(`${name} includes ${username}`);
          return false
        } else {
          return true
        }
      }
    }
    
  };

  useEffect(() => {
    const passed = handleUniqueValidation();
    if (passed === false) {
      inputRef.current.classList.add("ring-2","ring-red-450");
      spanRef.current.classList.remove("text-gray-200");
      spanRef.current.classList.add("text-red-450");
      setInfoText('*username taken')
      
    } else {
      inputRef.current.classList.remove("ring-2", "ring-red-450");
      spanRef.current.classList.remove("text-red-450");
      setInfoText("username may contain letters, digits and @ . + - _");
    }
  }, [username]);

  return (
    <div className="username_field flex flex-col ">
      <label htmlFor="username" className="mb-2">
        Username
      </label>
      <input
        id="username"
        className="h-12 rounded-md p-3 pl-3 bg-gray-200"
        placeholder="username"
        value={username}
        ref={inputRef}
        onChange={(e) => {
          string_validator(e.target.value, username, setUsername);
        }}
      />
      <span ref={spanRef} className="ml-1 font-mono mt-1 text-gray-300 font-light text-xs">
        {infoText}
      </span>
    </div>
  );
};

export default Username;
