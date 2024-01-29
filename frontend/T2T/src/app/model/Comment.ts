export interface Comment {
    cID?: string;
    text: string;
    postId: number;
    likes?: number;
    createdBy?: string;
    createdTime?: Date;
    parentCommentIds?: number[];
    childCommentIds?: number[];
    childComments?: Comment[];
}