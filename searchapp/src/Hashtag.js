import React, { Component } from 'react';
import PropTypes from 'prop-types';

class Hashtag extends Component {
	handleClick = () => {
		this.props.toggleHashtag(this.props.children);
	}
	render() {
		return (
			<div className={`hashtag ${this.props.active ? 'active' : ''}`} onClick={this.handleClick}>
				#{this.props.children}
			</div>
		);
	}
}

Hashtag.propTypes = {
	children: PropTypes.string,
	active: PropTypes.bool,
	toggleHashtag: PropTypes.func,
};

export default Hashtag;
