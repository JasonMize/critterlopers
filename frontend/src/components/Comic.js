import React, { Component } from 'react';

import {
  getComic,
} from '../actions/apiActions.js';

class Comic extends Component {
  constructor(props) {
    super(props);
    // let CancelToken = axios.CancelToken;

    this.state = {
      comic: [],
      pageNumber: 1,
    };
  }

  componentDidMount() {
    getComic(this, 3);
  }

  render () {
    let comic = this.state.comic;
    return (
      <div>
        Comic
        <div>{ comic.title }</div>
      </div>
    );
  }
}

export default Comic;