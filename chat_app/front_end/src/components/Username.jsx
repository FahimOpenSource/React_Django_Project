import React from "react";
import { useState, useEffect } from "react";
import axios from "axios";

const Username = ({ username, setUsername, string_validator }) => {
  const usernames = [];

  useEffect(() => {
    const base_url = "accounts/api/signup/";

    axios.get(base_url).then((res) => {
      const accounts = res.data;

      for (var account of accounts) {
        usernames.push(account.username);
        console.log(usernames);
      }
    });
  }, []);

  const handleUniqueValidation = () => {
    for (var account_username of usernames) {
      if (username === account_username) {
      }
    }
  };

  return (
    <div className="username_field flex flex-col ">
      <svg xmlns="http://www.w3.org/2000/svg">
        <symbol viewBox="0 0 24 24" id="unhappy">
          <path d="M0 0h24v24H0V0z" fill="none" />
          <circle cx="15.5" cy="9.5" r="1.5" />
          <circle cx="8.5" cy="9.5" r="1.5" />
          <path d="M12 14c-2.33 0-4.32 1.45-5.12 3.5h1.67c.69-1.19 1.97-2 3.45-2s2.75.81 3.45 2h1.67c-.8-2.05-2.79-3.5-5.12-3.5zm-.01-12C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" />
        </symbol>
      </svg>

      <svg xmlns="http://www.w3.org/2000/svg">
        <symbol viewBox="0 0 24 24">
          <path d="M0 0h24v24H0V0z" fill="none" />
          <circle cx="15.5" cy="9.5" r="1.5" />
          <circle cx="8.5" cy="9.5" r="1.5" />
          <path d="M12 16c-1.48 0-2.75-.81-3.45-2H6.88c.8 2.05 2.79 3.5 5.12 3.5s4.32-1.45 5.12-3.5h-1.67c-.7 1.19-1.97 2-3.45 2zm-.01-14C6.47 2 2 6.48 2 12s4.47 10 9.99 10C17.52 22 22 17.52 22 12S17.52 2 11.99 2zM12 20c-4.42 0-8-3.58-8-8s3.58-8 8-8 8 3.58 8 8-3.58 8-8 8z" />
        </symbol>
      </svg>

      <label htmlFor="username" className="mb-2">
        Username
      </label>
      <input
        id="username"
        className="h-12 rounded-md p-3 pl-3 bg-gray-200"
        placeholder="username"
        value={username}
        onChange={(e) => {
          string_validator(e.target.value, username, setUsername);
          handleUniqueValidation();
        }}
      />
      <span className="ml-1 font-mono mt-1 text-gray-200 font-light text-xs">
        username may contain letters, digits and @ . + - _
      </span>
    </div>
  );
};

export default Username;
