type ChartBarProps = {
	value: number;
};

const ChartBar: React.FC<ChartBarProps> = ({ value }) => {
	return (
		<div
			className={`w-[4.17px] h-[${value}px] bg-[#cb3cff] rounded-tl-[1px] rounded-tr-[1px]`}
		/>
	);
};

export default ChartBar;
