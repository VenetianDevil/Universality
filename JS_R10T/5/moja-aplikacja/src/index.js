import React from 'react';
import ReactDOM from 'react-dom';
import { Suspense, lazy } from 'react';
import * as serviceWorker from './serviceWorker';

const Name = React.lazy(() => import('./Name'));

class App extends React.Component {
    render() {
        return (
            <div >
                <Suspense fallback={<h6>Loading…</h6>}>
                    <Name />
                </Suspense>
            </div>
        );
    }
}

ReactDOM.render(<App />, document.getElementById('root'));

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
