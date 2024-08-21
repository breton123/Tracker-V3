import axios from "axios";

export async function getUser(email: string, password: string) {
	const response = await axios.post("http://localhost:8000/checkLogin", {
		username: email,
		email: email,
		password: password,
	});
	return response;
}
