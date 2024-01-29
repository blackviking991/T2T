import { Comment } from "./Comment";

export interface Post {
    pID?: string;
    title: string;
    desc: string;
    shortDesc: string;
    createdBy?: string;
    createdTime?: Date;
    likes?: number;
    tags?: String[];
    commentIds?: string[];
    childComments?: Comment[];
    forumName: string;
    views?: number;
    accessLevelsList?: string[];
}