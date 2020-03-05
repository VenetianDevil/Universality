import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import * as serviceWorker from './serviceWorker';

function App() {
    return (
        <Wraper>
            <div className='square'></div>
            <div className='square'></div>
            <div className='square'></div>
        </Wraper>
    )
}

class Wraper extends React.Component {
    render() {
        const childrenWithProps = React.Children.map(this.props.children, child => React.cloneElement(child, { style: { left: `${Math.random() * 91}%`, top: `${Math.random() * 91}%` }
}))
return (<div className="wraper">{childrenWithProps}</div>);
    }
}

ReactDOM.render(<App />, document.getElementsByTagName('body')[0]);

serviceWorker.unregister();
