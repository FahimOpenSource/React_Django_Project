import React from "react";
import axios from "axios";
import { useState, useRef, useEffect } from "react";
import useInputValidator from "../hooks/useInputValidator.jsx";

const Username = ({ username, setUsername, valid, setValid }) => {
  const inputRef = useRef();
  const [names, setNames] = useState({ list: [] });

  useEffect(() => {
    const base_url = "accounts/api/sign-up/";

    axios.get(base_url).then((res) => {
      setNames({ list: res.data });
    });
  }, []);

  useEffect(() => {
    if (username) {
      const span = inputRef.current.nextSibling;
      let taken = false;
      const invalid = /(?![@\.+\-_A-Za-z 0-9])./g.test(username);
      if (username !== "") {
        for (var name of names.list) {
          if (name.includes(username)) {
            taken = true;
          }
        }
      }

      if (taken === true || invalid === true) {
        inputRef.current.classList.add("ring-2", "ring-red-450");
        span.classList.remove("text-gray-200");
        span.classList.add("text-red-450");
        setValid({
          
          username: false,
        });
        if (taken === true) {
          span.innerHTML = "*username taken";
        } else if (invalid === true) {
          span.innerHTML =
            "*username may contain letters, digits and @ . + - _";
        }
      } else if (taken === false || invalid === false) {
        inputRef.current.classList.remove("ring-2", "ring-red-450");
        span.classList.remove("text-red-450");
        span.innerHTML = "username may contain letters, digits and @ . + - _";

        setValid({
          
          username: true,
        });
      }
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
          if (useInputValidator(e.target, username, valid)) {
            setUsername(e.target.value);
            setValid({
              
              username: true,
            });
          } else {
            setValid({
              
              username: false,
            });
          }
        }}
      />
      <span className="ml-1 font-mono mt-1 text-gray-300 font-light text-xs">
        username may contain letters, digits and @ . + - _
      </span>
    </div>
  );
};

export default Username;
