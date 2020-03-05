import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import Board from './Board';
import * as serviceWorker from './serviceWorker';

class App extends React.Component {
    constructor() {
        super();
        this.state = {
            board_size: null,
            form_submitted: false,
            end_game: false,
        }
        this.create_board = this.create_board.bind(this);
        this.handleChange = this.handleChange.bind(this);
        this.show_score = this.show_score.bind(this);
    }

    create_board(e) {
        e.preventDefault();
        // alert('board_size set to: ' + this.state.board_size)
        if (this.state.board_size !== null && this.state.board_size !== '')
            this.setState({ form_submitted: true })
    }

    handleChange(e) {
        this.setState({ board_size: e.target.value });
    }

    show_score(score) {
        const size = this.state.board_size;
        console.log(size);
        let result = (score / (size * size)).toFixed(3);
        this.setState({ score: result });
        this.setState({ end_game: true })
    }

    render() {
        if (this.state.form_submitted === false) {
            return (
                <form onSubmit={this.create_board} style={{width: '200px',
                        margin: '50px',
                        height: '25px',
                        textAlign: 'center',
                        padding: '1px'
                    }}>
                    <select value={this.state.board_size || ''} onChange={this.handleChange}>
                        <option></option>
                        <option value={4}>Easy 4x4 </option>
                        <option value={6}>Middle 6x6 </option>
                        <option value={8}>Hard 8x8 </option>
                    </select>
                    <button type='submit'>Start</button>
                </form>
            )
        }
        else {
            if (!this.state.end_game) {
                return (
                    <Board size={this.state.board_size} end_game={this.show_score} />
                )
            }
            else {
                return (
                    <div style={{
                        margin: '50px',
                        height: '25px',
                        backgroundColor: 'green',
                        borderRadius: '10px',
                        textAlign: 'center',
                        padding: '1px'
                    }}>
                        <h4 style={{margin: '0'}}>Twoj wynik: {this.state.score}</h4>
                    </div>
                )
            }
        }
    }
}

ReactDOM.render(<App />, document.getElementById('root'));
serviceWorker.unregister();