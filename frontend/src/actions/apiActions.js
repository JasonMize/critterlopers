import axios from 'axios';

export function getComic(react_component, pageNumber) {
  console.log('API');
  axios.get(
    '/api/comic/',
    { params: pageNumber, },
  ).then((data) => {
    console.log('API: getComic: data: ');
    // react_component.setState({comic: data.data.results});
  });
}