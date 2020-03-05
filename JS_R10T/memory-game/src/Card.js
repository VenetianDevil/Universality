import React from 'react';

class Card extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      number: this.props.number,
      display: 'none',
    }
    this.show_number = this.show_number.bind(this);
  }

  show_number(e) {
    this.props.action(this);
    e.preventDefault();
  }

  render() {
    return (
      <div onClick={this.show_number} style={{
        background: 'green',
        border: '1px black solid', width: '100px', height: '100px', textAlign: 'center',
      }}>
        <h1 style={{ display: `${this.state.display}` }}>{this.state.number}</h1>
      </div >
    );
  }
}

export default Card;
