import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            fields: {},
        };
        this.handleSubmit = this.handleSubmit.bind(this);
        this.handleChange = this.handleChange.bind(this);
    }

    handleValidation() {
        let fields = this.state.fields;
        let errors = {};
        let formIsValid = true;
        console.log(fields);

        if (typeof fields['number'] !== 'number') {
            formIsValid = false;
            document.getElementById('number').classList.add('error');
            document.getElementsByTagName('span')[0].textContent = 'zla warosc';
        }

        if (typeof fields['text'] !== 'string') {
            formIsValid = false;
            document.getElementById('text').classList.add('error');
            document.getElementsByTagName('span')[1].textContent = 'zla warosc';
        }

        this.setState({ errors: errors });
        return formIsValid;
    }

    handleChange(field, e) {
        let fields = this.state.fields;
        fields[field] = parseFloat(e.target.value) ? parseFloat(e.target.value) : e.target.value;
        this.setState({ fields });
        document.getElementById(field).classList.remove('error');
        document.getElementById(`span_${field}`).textContent=null;
    }

    handleSubmit(e) {
        if (this.handleValidation()) {
            alert('OK!');
        }
        e.preventDefault();
    }

    render() {
        const input_style = {
            borderRadius: "3px",
            border: '1px gray solid',
            width: '200px',
            margin: "0 5px"
        }
        const fieldset_style = {
            border: 'none',
            width: '200px',
            float: 'left'
        }
        return (
            <form onSubmit={this.handleSubmit.bind(this)}>
                <fieldset style={fieldset_style}>
                    <input id='number' style={input_style} placeholder='number' onChange={this.handleChange.bind(this, "number")} value={this.state.fields['number']}></input>
                    <br /><span id='span_number' style={{ fontSize: '10px', margin: '0 10px' }}></span>
                </fieldset>
                <fieldset style={fieldset_style}>
                    <input id='text' style={input_style} placeholder='text' onChange={this.handleChange.bind(this, "text")} value={this.state.fields['text']}></input>
                    <br /><span id='span_text' style={{ fontSize: '10px', margin: '0 10px' }}></span>
                </fieldset>
                <fieldset style={fieldset_style}>
                    <button style={{ backgroundColor: 'green', color: 'white', borderRadius: '5px' }} type='submit'>Send</button>
                </fieldset>
            </form>
        )
    }
}

ReactDOM.render(<Form />, document.getElementById('root'));

serviceWorker.unregister();
