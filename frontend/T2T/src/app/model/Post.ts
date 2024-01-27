export interface Post {
    id: number;
    title: string;
    desc: string;
    createdBy: string;
    createdTime: Date;
    tags: number[];
    likes: number;
    commentIds: number[];
    forumTag: number;
    views: number;
}