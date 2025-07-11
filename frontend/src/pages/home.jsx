import { useEffect, useState } from "react";
import api from "../api";
import Sudoku from "../components/Sudoku";
import "../styles/games.css"
import "../styles/Sudoku/Buttons.css"

const Home = () => {
  const [sudoku, setSudoku] = useState([]);

  useEffect(() => {
    getSudoku();
  }, []);


  const getSudoku = () => {
    api
      .get("api/sudoku/")
      .then((res) => res.data)
      .then((data) => {
        console.log(data);
        setSudoku(data);
      })
      .catch((err) => alert(err));
  };
  const createSudoku = (e) => {
    e.preventDefault();
    api
      .post("api/sudoku/")
      .then((res) => {
        if (res.status === 201) {
          getSudoku();
        } else alert("failed to make note");
      })
      .catch((err) => alert(err));
  };

  const deleteSudoku = (id) => {
    api
      .delete(`api/sudoku/delete/${id}/`)
      .then((res) => {
        if (res.status === 204) {
          getSudoku();
        } else alert("Failed to delete note");
      })
      .catch((err) => alert(err));
  };

  return (
    <><form style={{position: "absolute"}} onSubmit={(event) => createSudoku(event)}>
        <button type="submit" className="add">+</button>
      </form>
      <h1 className="headers">Sudoku</h1>
            
      <section className="games">
      {sudoku.map((board) => {
        return <Sudoku board={board} onDelete={deleteSudoku} key={board.id} />;
      })}


      </section>
            {/* 
      <h2>create a note</h2>

      <form onSubmit={createNote}>
        <input
          type="text"
          name="title"
          placeholder="title"
          onChange={(e) => setTitle(e.target.value)}
        />
        <br />
        <textarea
          required
          type="content"
          name="content"
          placeholder="content"
          value={Content}
          onChange={(e) => setContent(e.target.value)}
        ></textarea>
        <br />
        <button type="submit">submit</button>
      </form>*/}
    </>
  );
};
export default Home;
