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
	title: string;
	viewButton: (account: string) => void;
	settingsButton: (
		name: string,
		login: string,
		password: string,
		server: string,
		deposit: string,
		terminalFilePath: string
	) => void;
}

function capitalizeFirstLetter(str: string) {
	if (typeof str !== "string" || str.length === 0) {
		return str; // Return the original string if it's not a string or is empty
	}
	return str.charAt(0).toUpperCase() + str.slice(1);
}

const Table: React.FC<TableProps> = ({
	data,
	title,
	viewButton,
	settingsButton,
}) => {
	const [visibleColumns, setVisibleColumns] = useState<string[]>([]);
	const [filters, setFilters] = useState<boolean>(false);

	// Set default columns based on title
	React.useEffect(() => {
		if (title === "Accounts") {
			setVisibleColumns(["name", "login", "server", "enabled"]);
		} else if (title === "Sets") {
			setVisibleColumns([
				"magic",
				"name",
				"strategy",
				"profit",
				"maxDrawdown",
				"profitFactor",
				"returnOnDrawdown",
				"winRate",
				"avgTradeTime",
				"trades",
			]);
		} else if (title === "Open Sets") {
			setVisibleColumns([
				"magic",
				"name",
				"strategy",
				"profit",
				"maxDrawdown",
				"openDrawdown",
				"openEquity",
			]);
		} else {
			setVisibleColumns(Object.keys(data[0] || {}));
		}
	}, [data, title]);

	const handleColumnToggle = (column: string) => {
		setVisibleColumns((prev) =>
			prev.includes(column)
				? prev.filter((col) => col !== column)
				: [...prev, column]
		);
	};

	let headers = Object.keys(data[0] || {});

	if (title === "Accounts") {
		const newHeaderOrder = ["name", "login", "server", "enabled"];
		headers = newHeaderOrder;
	}

	// Reorder and filter data based on visible columns
	const reorderedData = data
		.filter((row) => {
			if (title === "Open Sets") {
				// Only keep rows where openEquity is not 0
				return row["openEquity"] != 0;
			}
			return true; // Keep all rows otherwise
		})
		.map((row) => {
			const reorderedRow: Record<string, any> = {};
			headers.forEach((header) => {
				if (visibleColumns.includes(header)) {
					reorderedRow[header] = row[header];
				}
			});
			return reorderedRow;
		});

	const toggleFilters = () => {
		if (filters) {
			setFilters(false);
		} else {
			setFilters(true);
		}
	};

	return (
		<div className="w-full  h-[737px] relative bg-[#0b1739] rounded-xl shadow border border-[#343a4e]">
			{/* Column Selector */}
			{filters ? (
				<button onClick={toggleFilters}>
					<div className="p-2 w-16 mt-5 ml-5 h-[30px] bg-[#cb3cff] rounded flex justify-center items-center gap-1.5 cursor-pointer">
						<div className="text-center text-white text-xs font-medium leading-[14px] ">
							Filters -
						</div>
					</div>
				</button>
			) : (
				<button onClick={toggleFilters}>
					<div className="p-2 mt-5 ml-5 w-16 h-[30px] bg-[#AEB9E1] rounded flex justify-center items-center gap-1.5 cursor-pointer">
						<div className="text-center text-white text-xs font-medium leading-[14px] ">
							Filters +
						</div>
					</div>
				</button>
			)}
			{filters ? (
				<div className="w-full flex">
					<div className="p-4 flex flex-wrap gap-5 w-1/2">
						{headers.map((header) => (
							<div
								key={header}
								className="flex items-center text-white">
								<input
									type="checkbox"
									checked={visibleColumns.includes(header)}
									onChange={() => handleColumnToggle(header)}
									className="mr-2"
								/>
								<label>{capitalizeFirstLetter(header)}</label>
							</div>
						))}
					</div>
				</div>
			) : (
				<span></span>
			)}

			{/* Table Header */}
			<div className="flex w-full justify-between p-7 font-semibold">
				<div className="text-white text-base font-bold leading-[18px]">
					{title}
				</div>
				<div className="">
					<span className="text-[#cb3cff] text-sm font-medium leading-[14px]">
						1 - 10
					</span>
					<span className="text-[#adb9e1] text-sm font-medium leading-[14px]">
						{" "}
						of {reorderedData.length}
					</span>
				</div>
			</div>

			{/* Table with custom scrollbar */}
			<SimpleBar style={{ maxHeight: "calc(100% - 64px)" }}>
				<table className="min-w-full w-auto  px-5 bg-[#0b1739] rounded-xl shadow border border-[#343a4e] border-t-0">
					<thead>
						<tr>
							{headers
								.filter((header) =>
									visibleColumns.includes(header)
								)
								.map((header) => (
									<th
										key={header}
										className="text-white text-center font-semibold">
										{capitalizeFirstLetter(header)}
									</th>
								))}
						</tr>
					</thead>
					<tbody>
						{reorderedData.map((row, index) => (
							<TableRow
								key={index}
								row={row}
								isOdd={index % 2 != 0}
								viewButton={viewButton}
								settingsButton={settingsButton}
							/>
						))}
					</tbody>
				</table>
			</SimpleBar>
		</div>
	);
};

export default Table;
