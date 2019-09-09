import React from 'react';
import PropTypes from 'prop-types';
import {
	MultiDropdownList,
	SingleDropdownRange,
	RangeSlider,
} from '@appbaseio/reactivesearch';

const SearchFilters = ({ currentHashtags, setHashtags, visible }) => (
	<div className={`flex column filters-container ${!visible ? 'hidden' : ''}`}>
		<div className="child m10">
			<MultiDropdownList
				componentId="hashtags"
				dataField="hashtags.keyword"
				placeholder="Select hashtags"
				title="Tweet Hashtags"
				filterLabel="Hashtags"
				size={1000}
				queryFormat="and"
				defaultSelected={currentHashtags}
				onValueChange={setHashtags}
			/>
		</div>
		<div className="child m10">
			<SingleDropdownRange
				componentId="created"
				dataField="created"
				placeholder="Tweet published"
				title="Created"
				filterLabel="Created"
				data={[
					{
						start: '2019-01-01T00:00:00Z',
						end: '2019-12-31T23:59:59Z',
						label: '2019',
					},
					{
						start: '2018-01-01T00:00:00Z',
						end: '2018-12-31T23:59:59Z',
						label: '2018',
					},
					{
						start: '2017-01-01T00:00:00Z',
						end: '2017-12-31T23:59:59Z',
						label: '2017',
					},
					{
						start: '2016-01-01T00:00:00Z',
						end: '2016-12-31T23:59:59Z',
						label: '2016',
					},
					{
						start: '2015-01-01T00:00:00Z',
						end: '2015-12-31T23:59:59Z',
						label: '2015',
					},
					{
						start: '2014-01-01T00:00:00Z',
						end: '2014-12-31T23:59:59Z',
						label: '2014',
					},
					{
						start: '2013-01-01T00:00:00Z',
						end: '2013-12-31T23:59:59Z',
						label: '2013',
					},
					{
						start: '2012-01-01T00:00:00Z',
						end: '2012-12-31T23:59:59Z',
						label: '2012',
					},
					{
						start: '2011-01-01T00:00:00Z',
						end: '2011-12-31T23:59:59Z',
						label: '2011',
					},
					{
						start: '2010-01-01T00:00:00Z',
						end: '2010-12-31T23:59:59Z',
						label: '2010',
					},
					{
						start: '2009-01-01T00:00:00Z',
						end: '2009-12-31T23:59:59Z',
						label: '2009',
					},
					{
						start: '2008-01-01T00:00:00Z',
						end: '2008-12-31T23:59:59Z',
						label: '2008',
					},
					{
						start: '2007-01-01T00:00:00Z',
						end: '2007-12-31T23:59:59Z',
						label: '2007',
					},
				]}
			/>
		</div>
		<div className="child m10">
			<RangeSlider
				componentId="nretweets"
				title="Retweets"
				dataField="nretweets"
				range={{ start: 0, end: 300000 }}
				showHistogram={false}
				rangeLabels={{
					start: '0 retweets',
					end: '300K retweets',
				}}
				innerClass={{
					label: 'range-label',
				}}
			/>
		</div>
		<div className="child m10">
			<RangeSlider
				componentId="nlikes"
				title="Likes"
				dataField="nlikes"
				range={{ start: 0, end: 180500 }}
				showHistogram={false}
				rangeLabels={{
					start: '0 Likes',
					end: '180K Likes',
				}}
				innerClass={{
					label: 'range-label',
				}}
			/>
		</div>
		<div className="child m10">
			<RangeSlider
				componentId="nreplies"
				title="Replies"
				dataField="nreplies"
				range={{ start: 0, end: 180500 }}
				showHistogram={false}
				rangeLabels={{
					start: '0 Replies',
					end: '180K Replies',
				}}
				innerClass={{
					label: 'range-label',
				}}
			/>
		</div>
	</div>
);

SearchFilters.propTypes = {
	currentHashtags: PropTypes.arrayOf(PropTypes.string),
	setHashtags: PropTypes.func,
	visible: PropTypes.bool,
};

export default SearchFilters;
