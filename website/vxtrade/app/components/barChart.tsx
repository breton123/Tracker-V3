import React from "react";
import {
	Bar,
	BarChart,
	CartesianGrid,
	Legend,
	ReferenceLine,
	ResponsiveContainer,
	Tooltip,
	XAxis,
	YAxis,
} from "recharts";

const data = [
	{ name: "08/08/24", profit: 300 },
	{ name: "09/08/24", profit: -145 },
	{ name: "10/08/24", profit: -100 },
	{ name: "11/08/24", profit: -8 },
	{ name: "12/08/24", profit: 100 },
	{ name: "13/08/24", profit: 100 },
	{ name: "14/08/24", profit: 100 },
];
const BarChartComponent = () => {
	return (
		<ResponsiveContainer width="100%" height={180}>
			<BarChart
				data={data}
				margin={{
					top: 20,
					right: 30,
					left: 30,
					bottom: 20,
				}}>
				<Tooltip />
				<ReferenceLine y={0} stroke="#000" />
				<Bar
					dataKey="profit"
					isAnimationActive={false}
					shape={(props) => {
						const { x, y, width, height, value, name } = props;
						const color = value >= 0 ? "#00C49F" : "#FF8042"; // Green for positive, red for negative
						return (
							<rect
								x={x}
								y={value >= 0 ? y : y + height} // Adjust y position for negative bars
								width={width}
								height={Math.abs(height)} // Ensure height is positive
								fill={color}
							/>
						);
					}}
				/>
			</BarChart>
		</ResponsiveContainer>
	);
};

export default BarChartComponent;
