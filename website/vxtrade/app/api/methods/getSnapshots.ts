import axios from "axios";

export async function getSnapshots(user: string, account: number) {
	try {
		const response = await axios.post(
			"http://localhost:8000/getSnapshots",
			{
				user: user,
				account: account,
			}
		);
		return response;
	} catch (error) {
		console.error("Error fetching accounts:", error);
		return []; // Return an empty array or handle the error as needed
	}
}
