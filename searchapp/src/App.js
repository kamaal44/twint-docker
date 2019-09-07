import React, { Component } from 'react';
import { ReactiveBase, DataSearch } from '@appbaseio/reactivesearch';

import Header from './Header';
import Results from './Results';

import theme from './theme';
import './App.css';

class App extends Component {
	constructor(props) {
		super(props);
		this.state = {
			currentHashtags: [],
		};
	}

	setHashtags = (currentHashtags) => {
		this.setState({
			currentHashtags: currentHashtags || [],
		});
	}

	toggleHashtag = (hashtag) => {
		const { currentHashtags } = this.state;
		const nextState = currentHashtags.includes(hashtag)
			? currentHashtags.filter(item => item !== hashtag)
			: currentHashtags.concat(hashtag);
		this.setState({
			currentHashtags: nextState,
		});
	}

	render() {
		return (
			<section className="container">
				<ReactiveBase
					app="twinttweets"
					url="http://localhost:9200"
					theme={theme}
				>
					<div className="flex row-reverse app-container">
						<Header currentHashtags={this.state.currentHashtags} setHashtags={this.setHashtags} />
						<div className="results-container">
							<DataSearch
								componentId="tweet"
								filterLabel="Search"
								dataField={['name', 'tweet', 'link', 'username', 'hashtags']}
								placeholder="Search tweets"
								iconPosition="left"
								autosuggest={true}
								fuzziness={0}
  							    debounce={50}
								URLParams
								className="data-search-container results-container"
								innerClass={{
									input: 'search-input',
								}}
							/>
							<Results currentHashtags={this.state.currentHashtags} toggleHashtag={this.toggleHashtag} />
						</div>
					</div>
				</ReactiveBase>
			</section>
		);
	}
}

export default App;
