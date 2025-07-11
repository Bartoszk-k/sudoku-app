import { useState } from "react";
import "../styles/Sudoku/sudokuBoard.css";
import React from "react";

const SudokuBoard = ({ board }) => {
  
  const [inputs, setInputs] = useState(
    Array(9)
      .fill(null)
      .map(() => Array(9).fill(""))
  );
  const [correctStates, setCorrectStates] = useState(
    Array(9)
      .fill(null)
      .map(() => Array(9).fill(null))
  );
const handleChange = (e, rowIdx, colIdx) => {
                const value = e.target.value;

                const updatedInputs = inputs.map((row, i) =>
                  i === rowIdx
                    ? row.map((cell, j) => (j === colIdx ? value : cell))
                    : row
                );
                setInputs(updatedInputs);

                const correctValue = board.completed[rowIdx][colIdx];
                const isCorrect = parseInt(value, 10) === correctValue;

                const updatedCorrectStates = correctStates.map((row, i) =>
                  i === rowIdx
                    ? row.map((cell, j) => (j === colIdx ? isCorrect : cell))
                    : row
                );
                setCorrectStates(updatedCorrectStates);

              };
  return (
    <div className="Sudoku-Board" border="1">
      {board.board.map((row, i) => {
        const isBlockSeparator = (i + 1) % 3 === 0;
        return (
          <React.Fragment key={`row-${i}`}>
            {row.map((field, j) => {
              const isBlockSeparator1 = (j + 1) % 3 === 0;
              
              const cellState = correctStates[i][j];
              return (
                <React.Fragment key={`cell-${i}-${j}`}>
                  <section
                    style={{
                      backgroundColor:
                        cellState  === true
                          ? "#d4edda"
                          : cellState  === false
                          ? "#f8d7da"
                          : "white",
                    }}
                  >
                    {field !== 0 ? (
                      field
                    ) : (
                      <input
                        type="text"
                        className="field"
                        maxLength={1}
                        value={inputs[i][j]}
                        onChange={(e) => handleChange(e, i, j)}
                      />
                    )}
                  </section>
                  {isBlockSeparator1 && j !== 8 && <div>|</div>}
                </ React.Fragment>
              );
            })}
            {isBlockSeparator && i !== 8 && (
              <>
                <div>-</div>
                <div>-</div>
                <div>-</div>
                <div>+</div>
                <div>-</div>
                <div>-</div>
                <div>-</div>
                <div>+</div>
                <div>-</div>
                <div>-</div>
                <div>-</div>
              </>
            )}
          </React.Fragment>
        );
      })}
    </div>
  );
};
export default SudokuBoard;
