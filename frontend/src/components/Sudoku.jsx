import SudokuBoard from "./SudokuBoard";
import "../styles/Sudoku/sudokuBoard.css"
import "../styles/Sudoku/Buttons.css"
import { useNavigate } from "react-router-dom";

const Sudoku = ({ board, onDelete }) => {
  const navigate = useNavigate()
  const formatDate = new Date(board.created_at).toLocaleDateString("pl-PL");

  return (
    <div className="SudokuCart">
      <div className="Sudoku"><SudokuBoard board={board.Boards} /></div>
      <p className="data">{formatDate}</p>
      <button className="delete trnsform" onClick={() => onDelete(board.id)}>-</button>
    </div>
  );
};

export default Sudoku;
