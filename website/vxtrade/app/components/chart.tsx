import React from "react";
import {
	CartesianGrid,
	Legend,
	Line,
	LineChart,
	ResponsiveContainer,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

// Sample data with multiple data keys for different lines

const Chart = ({ data, magics, title }) => {
	return (
		<div className="w-full backdrop-blur-[120px] font-mona bg-[#0b1739] rounded-tl-xl rounded-bl-xl border border-[#343a4e]">
			<div className="flex w-full px-5 ml-20 py-5 justify-between">
				<div className="flex flex-col">
					<h1 className="text-white font-semibold text-lg">
						{title}
					</h1>
				</div>
			</div>
			<ResponsiveContainer
				width="100%"
				height={500}
				className="pr-5 pt-5">
				<LineChart data={data}>
					<XAxis dataKey="time" />
					<YAxis />
					<Tooltip />
					<Legend />
					{/* Line for Profit */}
					{magics.map((magic: string, index: number) => {
						// Generate a random color
						const randomColor = `#${Math.floor(
							Math.random() * 16777215
						).toString(16)}`;

						return (
							<Line
								type="monotone"
								dataKey={magic}
								stroke={randomColor}
								strokeWidth={2}
								dot={false}
								key={index}
							/>
						);
					})}
				</LineChart>
			</ResponsiveContainer>
		</div>
	);
};

export default Chart;
