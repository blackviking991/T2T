export interface User {
    id: number;
    firstName: string;
    lastName: string;
    about: string;
    email: string;
    points: number;
    interestTags: number[];
    postIds: number[];
    commentIds: number[];
    forumTags: number[];
    joiningDate: Date;
}