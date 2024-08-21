import React, { useState } from "react";
import SimpleBar from "simplebar-react";
import "simplebar-react/dist/simplebar.min.css"; // Import SimpleBar CSS
import { PassThrough } from "stream";
import TableRow from "./tableRow";

// Define the type for the data object
type DataRow = {
	[key: string]: string | number | boolean | React.ReactNode;
};

interface TableProps {
	data: DataRow[];
}

const SetsTable: React.FC<TableProps> = ({ data }) => {
	return (
		<div className="">
			<table className="">
				<thead>
					<tr>
						<th>Magic</th>
						<th>Name</th>
						<th>Symbol</th>
					</tr>
				</thead>
				<tbody>
					{data.map((row, index) => (
						<tr
							className="text-white text-base font-bold leading-[18px]"
							key={row.index}>
							<td>{row.magic}</td>
							<td>{row.setName}</td>
							<td>{row.symbol}</td>
						</tr>
					))}
				</tbody>
			</table>
		</div>
	);
};

export default SetsTable;
