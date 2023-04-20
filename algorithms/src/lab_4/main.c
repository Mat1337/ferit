//
// Created by mat on 4/20/23.
//
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <timings.h>

typedef struct branch {
    char letter;

    struct branch *left;
    struct branch *right;
} branch_t;

static void tree_add(branch_t **branch, char letter) {
    if (*branch == NULL) {
        *branch = (branch_t *) malloc(sizeof(branch_t));
        if (*branch == NULL)
            return;

        (*branch)->letter = letter;
        (*branch)->left = NULL;
        (*branch)->right = NULL;
    } else {
        const char current_letter = (*branch)->letter;
        if (current_letter == letter)
            return;

        if (current_letter > letter) {
            tree_add(&(*branch)->left, letter);
            return;
        }

        tree_add(&(*branch)->right, letter);
    }
}

static void tree_nld(const branch_t *branch) {
    if (branch == NULL)
        return;

    printf("%c ", branch->letter);
    tree_nld(branch->left);
    tree_nld(branch->right);
}

static void tree_lnd(const branch_t *branch) {
    if (branch == NULL)
        return;

    tree_nld(branch->left);
    printf("%c ", branch->letter);
    tree_nld(branch->right);
}

static void tree_ldn(const branch_t *branch) {
    if (branch == NULL)
        return;

    tree_nld(branch->left);
    tree_nld(branch->right);
    printf("%c ", branch->letter);
}

static void tree_free(branch_t *branch) {
    branch_t *left = branch->left;
    branch_t *right = branch->right;

    free(branch);

    if (left != NULL)
        tree_free(left);
    if (right != NULL)
        tree_free(right);
}

int main(void) {
    const char *name = "Matko Vukovic";

    branch_t *tree = NULL;
    for (int i = 0; i < strlen(name); ++i)
        tree_add(&tree, name[i]);

    printf("  ");
    section_start("NLD");
    tree_nld(tree);
    printf("\n");
    section_end("NLD");

    section_start("LND");
    tree_lnd(tree);
    printf("\n");
    section_end("LND");

    section_start("LDN");
    tree_ldn(tree);
    printf("\n");
    section_end("LDN");

    tree_free(tree);
    return 0;
}