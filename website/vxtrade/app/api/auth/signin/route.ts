import { compare } from "bcryptjs";
import jwt from "jsonwebtoken";
import { NextResponse } from "next/server";
import { getUser } from "../../methods/getUser";

export async function POST(request: Request) {
	const { email, password } = await request.json();

	// Ensures email and password have been provided
	if (!email || !password) {
		return NextResponse.json(
			{ message: "Email and password are required." },
			{ status: 400 }
		);
	}

	// Attempts to get the user from db
	let user = await getUser(email, password);
	console.log(user.data);

	// If user doesnt exist
	if (user == null) {
		return NextResponse.json(
			{ message: "Invalid email or password." },
			{ status: 401 }
		);
	}

	// Generate a JWT token
	const token = jwt.sign(
		{
			userId: user.data.username,
			email: user.data.email,
			type: user.data.type,
		},
		process.env.JWT_SECRET as string,
		{ expiresIn: "1h" }
	);

	return NextResponse.json({ token });
}
