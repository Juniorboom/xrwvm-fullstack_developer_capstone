import React, { useState } from "react";
import "./Register.css";

import user_icon from "../assets/person.png";
import email_icon from "../assets/email.png";
import password_icon from "../assets/password.png";
import close_icon from "../assets/close.png";


const Register = () => {

  // State variables for form inputs
  const [userName, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [email, setEmail] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");


  // Redirect to the homepage
  const goHome = () => {
    window.location.href = window.location.origin;
  };


  // Handle registration form submission
  const register = async (e) => {

    e.preventDefault();

    const register_url =
      window.location.origin + "/djangoapp/register";


    // Send POST request to registration endpoint
    const res = await fetch(register_url, {

      method: "POST",

      headers: {
        "Content-Type": "application/json",
      },

      body: JSON.stringify({

        userName: userName,
        password: password,
        firstName: firstName,
        lastName: lastName,
        email: email

      }),

    });


    const json = await res.json();


    // Registration successful
    if (json.status) {

      // Save username in the browser session
      sessionStorage.setItem(
        "username",
        json.userName
      );

      // Redirect to homepage
      window.location.href =
        window.location.origin;

    }


    // Username is already registered
    else if (
      json.error === "Already Registered"
    ) {

      alert(
        "The user with the same username is already registered."
      );

      window.location.href =
        window.location.origin;

    }

  };


  return (

    <div
      className="register_container"
      style={{ width: "50%" }}
    >


      {/* Registration header */}

      <div
        className="header"
        style={{
          display: "flex",
          flexDirection: "row",
          justifyContent: "space-between"
        }}
      >

        <span
          className="text"
          style={{ flexGrow: "1" }}
        >
          Sign Up
        </span>


        <div
          style={{
            display: "flex",
            flexDirection: "row",
            alignSelf: "start"
          }}
        >

          <a
            href="/"
            onClick={goHome}
          >

            <img
              style={{ width: "1cm" }}
              src={close_icon}
              alt="Close"
            />

          </a>

        </div>

      </div>


      {/* Registration form */}

      <form onSubmit={register}>

        <div className="inputs">


          {/* Username */}

          <div className="input">

            <img
              src={user_icon}
              className="img_icon"
              alt="Username"
            />

            <input
              type="text"
              name="username"
              placeholder="Username"
              className="input_field"
              required
              onChange={
                (e) =>
                  setUserName(e.target.value)
              }
            />

          </div>


          {/* First name */}

          <div className="input">

            <img
              src={user_icon}
              className="img_icon"
              alt="First Name"
            />

            <input
              type="text"
              name="first_name"
              placeholder="First Name"
              className="input_field"
              required
              onChange={
                (e) =>
                  setFirstName(e.target.value)
              }
            />

          </div>


          {/* Last name */}

          <div className="input">

            <img
              src={user_icon}
              className="img_icon"
              alt="Last Name"
            />

            <input
              type="text"
              name="last_name"
              placeholder="Last Name"
              className="input_field"
              required
              onChange={
                (e) =>
                  setLastName(e.target.value)
              }
            />

          </div>


          {/* Email */}

          <div className="input">

            <img
              src={email_icon}
              className="img_icon"
              alt="Email"
            />

            <input
              type="email"
              name="email"
              placeholder="Email"
              className="input_field"
              required
              onChange={
                (e) =>
                  setEmail(e.target.value)
              }
            />

          </div>


          {/* Password */}

          <div className="input">

            <img
              src={password_icon}
              className="img_icon"
              alt="Password"
            />

            <input
              type="password"
              name="password"
              placeholder="Password"
              className="input_field"
              required
              onChange={
                (e) =>
                  setPassword(e.target.value)
              }
            />

          </div>

        </div>


        {/* Register button */}

        <div className="submit_panel">

          <input
            className="submit"
            type="submit"
            value="Register"
          />

        </div>

      </form>

    </div>

  );

};


export default Register;