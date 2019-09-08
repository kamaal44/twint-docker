import React from 'react';
import { SelectedFilters, ReactiveList } from '@appbaseio/reactivesearch';
import PropTypes from 'prop-types';

import Hashtag from './Hashtag';

const onResultStats = (results, time) => (
	<div className="flex justify-end">
		{results} results found {/*in {time}ms*/}
	</div>
);

const onData = (data, currentHashtags, toggleHashtag) => (
	<div className="result-item" key={data.id}>
		<div className="flex justify-center align-center result-card-header">
			<a className="link" href={data.link} target="_blank" rel="noopener noreferrer">
				<div className="flex wrap">
					<div>{data.username}/</div>
					<div>{data.name}</div>
				</div>
			</a>
		</div>
		<div className="m10-0">{data.tweet}</div>
		<div className="flex wrap justify-center">
			{
				data.hashtags.slice(0, 7)
					.map(item => (
						<Hashtag
							key={item}
							active={currentHashtags.includes(item)}
							toggleHashtag={toggleHashtag}
						>
							{item}
						</Hashtag>
					))
			}
		</div>
		<div className="flex">
			<div><div className="btn card-btn"><i className="card-icon fas fa-star" />{data.nlikes}</div></div>
			<div><div className="btn card-btn"><i className="card-icon fas fa-code-branch" />{data.nreplies}</div></div>
			<div><div className="btn card-btn"><i className="card-icon fas fa-eye" />{data.nretweets}</div></div>
		</div>
	</div>
);

const Results = ({ toggleHashtag, currentHashtags }) => (
	<div className="result-list">
		<SelectedFilters className="m1" />
		<ReactiveList
			componentId="results"
			dataField="id"
			onData={data => onData(data, currentHashtags, toggleHashtag)}
			onResultStats={onResultStats}
			react={{
				and: [		'nlikes',
							'nreplies',
							'nretweets'],
			}}
			pagination
			innerClass={{
				list: 'result-list-container',
				pagination: 'result-list-pagination',
				resultsInfo: 'result-list-info',
				poweredBy: 'powered-by',
			}}
			size={6}
			sortOptions={[
				{
					label: 'Best Match',
					dataField: '_score',
					sortBy: 'desc',
				},
				{
					label: 'Most likes',
					dataField: 'nlikes',
					sortBy: 'desc',
				},
				{
					label: 'Fewest likes',
					dataField: 'nlikes',
					sortBy: 'asc',
				},
				{
					label: 'Most Replies',
					dataField: 'nreplies',
					sortBy: 'desc',
				},
				{
					label: 'Fewest Replies',
					dataField: 'nreplies',
					sortBy: 'asc',
				},

				{
					label: 'Most Retweet',
					dataField: 'nretweets',
					sortBy: 'desc',
				},
				{
					label: 'Fewest Retweet',
					dataField: 'nretweets',
					sortBy: 'asc',
				}
			]}
		/>
	</div>
);

Results.propTypes = {
	toggleHashtag: PropTypes.func,
	currentHashtags: PropTypes.arrayOf(PropTypes.string),
};

export default Results;
