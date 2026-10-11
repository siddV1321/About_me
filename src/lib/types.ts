export type Project={id:string;name:string;category:string;status:string;description:string;link:string};
export type PortfolioContent={
 name:string;headline:string;intro:string;location:string;className:string;session:string;
 halfYearly:string;cgpa:string;gpa:string;academicNote:string;focus:string;skills:string[];
 projects:Project[];about:string;contactLabel:string;contactUrl:string;updatedAt?:string;
};