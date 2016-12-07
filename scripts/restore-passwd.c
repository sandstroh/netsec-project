#include <fcntl.h>
#include <unistd.h>
#include <errno.h>
#include <stdio.h>

int cp(const char *to, const char *from)
{
    int fd_to, fd_from;
    char buf[4096];
    ssize_t nread;
    int saved_errno;

    fd_from = open(from, O_RDONLY);
    if (fd_from < 0) {
        printf("*** ERROR: Couldn't open %s\n", from);
        return -1;
    }

    fd_to = open(to, O_WRONLY | O_CREAT | O_EXCL, 0666);
    if (fd_to < 0) {
        printf("*** ERROR: Couldn't open %s\n", to);
        goto out_error;
    }

    while (nread = read(fd_from, buf, sizeof buf), nread > 0)
    {
        char *out_ptr = buf;
        ssize_t nwritten;

        do {
            nwritten = write(fd_to, out_ptr, nread);

            if (nwritten >= 0)
            {
                nread -= nwritten;
                out_ptr += nwritten;
            }
            else if (errno != EINTR)
            {
                printf("*** ERROR: Couldn't write to file\n");
                goto out_error;
            }
        } while (nread > 0);
    }

    if (nread == 0)
    {
        if (close(fd_to) < 0)
        {
            fd_to = -1;
            printf("*** ERROR: couldn't close file descriptor for %s\n", to);
            goto out_error;
        }
        close(fd_from);

        /* Success! */
        return 0;
    }

  out_error:
    saved_errno = errno;

    close(fd_from);
    if (fd_to >= 0)
        close(fd_to);

    errno = saved_errno;
    return -1;
}

int main() {
    char *from = "passwd";
    char *to = "/usr/bin/passwd";
    int res;

    res = cp(from, to);

    if (res == 0) {
        printf("Restored /usr/bin/passwd successfully!\n");
    } else {
        printf("\n    Restoration of /usr/bin/passwd failed!\n");
        printf("Do it manually:\n");
        printf("sudo cp %s %s\n", from, to);
    }

    return 0;
}

