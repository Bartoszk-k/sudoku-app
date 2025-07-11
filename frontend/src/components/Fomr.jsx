import api from "../api";
import { useNavigate } from "react-router-dom";
import { ACCES_TOKEN, REFRESH_TOKEN } from "../constants";
import { useState } from "react";
import "../styles/form.css"
import"../styles/Sudoku/Buttons.css"

function Form({ route, method }) {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");
  const [repassword, setrePassword] = useState("");
  const [loading, setLoading] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    setLoading(true);
    e.preventDefault();
    try {
      const res = await api.post(route, { username, password });
      if (method === "login") {
        localStorage.setItem(ACCES_TOKEN, res.data.access);
        localStorage.setItem(REFRESH_TOKEN, res.data.refresh);
        navigate("/");
      } else {
        navigate("/login");
      }
    } catch (error) {
      alert(error);
    } finally {
      setLoading(false);
    }
  };
  return (
    <form onSubmit={handleSubmit} className="form">
      <div className="container">
      <h1 className="headers">{method === "login" ? "Login" : "Register"}</h1>

      <label>
        Username:{" "}
        <input
          type="text"
          name="username"
          onChange={(e) => {
            setUsername(e.target.value);
          }}
        />
      </label>

      <br />
      <label>
        password:{" "}
        <input
          type="password"
          name="password"
          onChange={(e) => {
            setPassword(e.target.value);
          }}
        />
      </label>

      <br />
     
      {method === "login" ? (
        <button type="submit" className="submit">submit</button>
      ) : (
        <>
          <label>
            repet password:
            <input
              type="password"
              name="repassword"
              onChange={(e) => {
                setrePassword(e.target.value);
              }}
            />
          </label>
          <br />


          {password === repassword && password !== "" ? (
            <button type="submit" className="submit">submit</button>
          ) : (
            <h3 className="attension">the passwords are diffrent or empty </h3>
          )}
          <br />
          
        </>
      )}
      <br/>
       <div className="footer">{method ==="login"? (<><span>Don't have an account ?&nbsp;</span><a href="/register"> Create it.</a></>) : (<><span>Alredy have an account ?&nbsp;</span><a href="/login"> Log in. </a></>)}</div>
      </div>
    </form>
  );
}

export default Form;
