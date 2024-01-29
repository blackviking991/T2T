export interface User {
    firstName: string;
    lastName: string;
    email: string;
    about: string;
    org: string[];
    points?: number;
    postCommentCount?: number;
    postCommentLikes?: number;
    postViewCount?: number;
    commentIds?: number[];
    postIds?: number[];
    postViews?: number;
    interestTags?: string[];
    roles?: string[];
    likedPosts?: number[];
    likedComments?: number[];
}