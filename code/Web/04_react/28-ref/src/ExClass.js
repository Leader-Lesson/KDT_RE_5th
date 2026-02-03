import React, { Component } from 'react';

export default class ExClass extends Component {
  state = {
    comments: [
      {
        writer: '민수',
        title: '안뇽',
      },
      {
        writer: '지민',
        title: '하이하이',
      },
    ],
  };
  writerRef = React.createRef();
  titleRef = React.createRef();

  checkInputValue = () => {
    const inputWriter = this.writerRef.current.value;
    const inputTitle = this.titleRef.current.value;
    if (inputWriter.trim().length === 0) {
      this.writerRef.current.focus();
      return false;
    }

    if (inputTitle.trim().length === 0) {
      this.titleRef.current.focus();
      return false;
    }

    return true;
  };

  addComment = () => {
    if (!this.checkInputValue()) {
      return;
    }

    const newComment = {
      writer: this.writerRef.current.value,
      title: this.titleRef.current.value,
    };

    this.setState((prevState) => ({
      comments: [...prevState.comments, newComment],
    }));

    this.writerRef.current.value = '';
    this.titleRef.current.value = '';
  };

  render() {
    const { comments } = this.state;
    return (
      <div>
        <form>
          <label htmlFor="writer">작성자:</label>
          <input id="writer" type="text" name="writer" ref={this.writerRef} />
          <label htmlFor="title">제목:</label>
          <input id="title" type="text" name="title" ref={this.titleRef} />
          <button type="button" onClick={this.addComment}>
            작성
          </button>
        </form>

        <h3>전체 댓글 목록</h3>
        <table border={1} style={{ margin: '30px auto', width: '500px' }}>
          <thead>
            <tr>
              <th>번호</th>
              <th>제목</th>
              <th>작성자</th>
            </tr>
          </thead>
          <tbody>
            {comments.map((cmt, idx) => (
              <tr key={idx + 1}>
                <td>{idx + 1}</td>
                <td>{cmt.title}</td>
                <td>{cmt.writer}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    );
  }
}
