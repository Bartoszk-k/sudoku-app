const Note = ({ note, onDelete }) => {
    const fromatDate = new Date(note.created_at).toLocaleDateString("pl-PL")

  return(
  <div>
    <h3>{note.Title}</h3>
    <p>{note.Content}</p>
    <p>{fromatDate}</p>
    <button onClick={() => onDelete(note.id)}>delete</button>
  </div>);
};
export default Note;
