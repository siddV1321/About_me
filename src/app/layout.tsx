import type { Metadata } from "next";
import "./globals.css";
export const metadata: Metadata = {
 title:"Siddharth Verma | Student & AI Research Explorer",
 description:"A portfolio of learning, software projects, research interests, and experiments by Siddharth Verma.",
 robots:{index:true,follow:true}
};
export default function RootLayout({children}:{children:React.ReactNode}) {
 return <html lang="en"><body>{children}</body></html>;
}