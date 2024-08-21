import axios from "axios";

export async function getAccounts(user: string) {
	try {
		const response = await axios.post("http://localhost:8000/getAccounts", {
			user: user,
		});
		console.log(response);
		return response;
	} catch (error) {
		console.error("Error fetching accounts:", error);
		return []; // Return an empty array or handle the error as needed
	}
}
