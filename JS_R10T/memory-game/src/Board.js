import React from 'react';
import Card from './Card';

class Board extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            size: this.props.size,
            shown: [],
            cards: [],
            score: 0,
        }

        this.pressed_card = this.pressed_card.bind(this);
        this.componentDidMount = this.componentDidMount.bind(this);
        this.componentDidUpdate = this.componentDidUpdate.bind(this);
        this.create_cards = this.create_cards.bind(this);
    }

    pressed_card(card) {
        if (this.state.shown.length < 2 && card.state.display === 'none') {
            console.log("I'm the board!\n pressed card has nr: " + card.state.number);
            card.setState({ display: 'block' });
            this.setState({ shown: this.state.shown.concat(card) });
            this.setState({ score: this.state.score + 1 });
            console.log(this.state.score)

        }
        // console.info(this.state.shown);
    }

    componentDidMount() {
        this.create_cards();
    }

    componentDidUpdate() {
        var time_id = setTimeout(function () {
            if (this.state.shown.length === 2) {
                if (this.state.shown[0].state.number === this.state.shown[1].state.number) {
                    for (let i = 0; i < this.state.cards.length; i++) {
                        if (this.state.shown[0]._reactInternalFiber.key === this.state.cards[i].key || this.state.shown[1]._reactInternalFiber.key === this.state.cards[i].key) {
                            this.state.cards.splice(i, 1);
                            i--;
                        }
                    }
                    this.forceUpdate();
                }
                else {
                    this.state.shown[0].setState({ display: 'none' });
                    this.state.shown[1].setState({ display: 'none' });
                }
                this.state.shown.splice(0, 2);
            }

            if (this.state.cards.length === 0) {
                console.log(this.state.score)
                this.props.end_game(this.state.score);
                clearTimeout(time_id);
            }
        }.bind(this), 1500);
    }

    create_cards() {
        console.log('renderuje karty')
        const size = this.state.size;
        if (size * size % 2 === 0) {
            let cards = [];
            let no_of_pairs = this.state.size * this.state.size / 2;
            for (let i = 0; i < no_of_pairs; i++) {
                cards.push(<Card key={`no_${i}a`} number={i} action={this.pressed_card} />)
                cards.push(<Card key={`no_${i}b`} number={i} action={this.pressed_card} />)
            }
            cards.sort(function () {
                return .5 - Math.random();
            });
            console.info('cards shuffled')
            this.setState({ cards: cards });
        }
        else {
            alert('zly rozmiar tablicy')
            console.error('nieparzysta ilsc elementow, podaj inny rozmiar tablicy')
        }
    }

    render() {
        console.log('renderuje tablice')

        return (
            <div style={{
                width: `${this.state.size * 102}px`, height: `${this.state.size * 102}px`, border: '1px black solid',
                display: 'grid', gridTemplateColumns: `repeat(${this.state.size}, 102px)`,
                gridTemplateRows: `repeat(${this.state.size}, 102px)`
            }}>
                {this.state.cards}
            </div>
        )
    }
}

export default Board;