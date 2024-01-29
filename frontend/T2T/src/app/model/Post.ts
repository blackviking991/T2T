import { Tag } from "./Tag";

export interface Post {
    id: number;
    title: string;
    desc: string;
    createdBy: string;
    createdAt: Date;
    tags: String[];
    likes: number;
    commentIds: number[];
    forumTag: number;
    views: number;
}