import { useState } from "react";

export default function Ex3() {
  const [inputWriter, setInputWriter] = useState("");
  const [inputTitle, setInputTitle] = useState("");
  const [comment, setComment] = useState([
    {
      writer: "민수",
      title: "안뇽",
    },
    {
      writer: "지민",
      title: "하이하이",
    },
    {
      writer: "희수",
      title: "멋쟁이",
    },
  ]);
  const [inputSearch, setInputSearch] = useState("");
  const [searchType, setSearchType] = useState("writer");
  const [result, setResult] = useState([]);

  const addComment = () => {
    let newComment = {
      writer: inputWriter,
      title: inputTitle,
    };

    setComment([...comment, newComment]);
    setInputWriter("");
    setInputTitle("");
  };
  const selectSearchType = (e) => {
    setSearchType(e.target.value);
  };

  const searchComment = () => {
    const searchResult = comment.filter((value) => {
      if (value[searchType].includes(inputSearch)) return value;
      else return null;
    });

    setResult(searchResult);
    setInputSearch("");
  };
  return (
    <div>
      <form>
        <label htmlFor="writer">작성자:</label>
        <input
          id="writer"
          type="text"
          name="writer"
          value={inputWriter}
          onChange={(e) => setInputWriter(e.target.value)}
        />
        <label htmlFor="title">제목:</label>
        <input
          id="title"
          type="text"
          name="title"
          value={inputTitle}
          onChange={(e) => setInputTitle(e.target.value)}
        />
        <button type="button" onClick={addComment}>
          작성
        </button>
      </form>
      <select onChange={selectSearchType}>
        <option value="writer">작성자</option>
        <option value="title">제목</option>
      </select>
      <input
        type="text"
        placeholder="검색어"
        value={inputSearch}
        onChange={(e) => setInputSearch(e.target.value)}
      />
      <button onClick={searchComment}>검색</button>

      <table border={1} style={{ marginTop: "30px", width: "500px" }}>
        <thead>
          <tr>
            <th>번호</th>
            <th>제목</th>
            <th>작성자</th>
          </tr>
        </thead>
        <tbody>
          {comment.map((value, idx) => {
            return (
              <tr key={idx + 1}>
                <td>{idx + 1}</td>
                <td>{value.title}</td>
                <td>{value.writer}</td>
              </tr>
            );
          })}
        </tbody>
      </table>

      <h3>검색 결과</h3>
      {result.length > 0 ? (
        <table border={1} style={{ marginTop: "30px", width: "500px" }}>
          <thead>
            <tr>
              <th>번호</th>
              <th>제목</th>
              <th>작성자</th>
            </tr>
          </thead>
          <tbody>
            {result.map((value, idx) => {
              return (
                <tr key={idx + 1}>
                  <td>{idx + 1}</td>
                  <td>{value.title}</td>
                  <td>{value.writer}</td>
                </tr>
              );
            })}
          </tbody>
        </table>
      ) : (
        <div>검색 결과가 없습니다</div>
      )}
    </div>
  );
}
