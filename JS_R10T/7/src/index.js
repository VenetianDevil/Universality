import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';

class Cat extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        error: null,
        isLoaded: false,
        cats: []
      };
    }
  
    componentDidMount() {
      fetch(" https://api.thecatapi.com/v1/images/search")
        .then(res => res.json())
        .then(
          (result) => {
            this.setState({
              isLoaded: true,
              cats: result
            });
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }
  
    render() {
      const { error, isLoaded, cats } = this.state;
      if (error) {
        return <div>Błąd: {error.message}</div>;
      } else if (!isLoaded) {
        return <div>Ładowanie...</div>;
      } else {
        return (
            <img src={cats[0].url} alt = 'cat'/>
        );
      }
    }
  }

ReactDOM.render(<Cat />, document.getElementById('root'));

serviceWorker.unregister();
